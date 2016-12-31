from EC2Facade import EC2Facade


class EC2Manager:
    """

    """

    def __init__(self, max_bid, threshold, min_count, max_count, price_watcher):
        """

        Args:
            max_bid:
            threshold:
            min_count:
            max_count:
        """
        self.price_watcher = price_watcher
        self.prices = {}
        self.threshold_types = set()
        self.max_bid = max_bid
        self.threshold = threshold
        self.min_count = min_count
        self.max_count = max_count
        self.running = []
        self.update_prices()
        self.create_mandatory_instances()

    def create_mandatory_instances(self):
        count = self.additional_instances_count(self.min_count)
        inst_type = self.get_cheapest_type()[0]
        self.add_instances(count, inst_type)

    def create_optional_instances(self):
        inst_type = self.get_cheapest_type()[0]
        if self.prices[inst_type] <= self.threshold:
            count = self.additional_instances_count(self.max_count)
            self.add_instances(count, inst_type)

    def update_prices(self):
        self.prices = self.price_watcher.get_prices()
        self.update_threshold_types()

    def update_threshold_types(self):
        for (inst_type, price) in self.prices.items():
            if price <= self.threshold:
                self.threshold_types.discard(inst_type)
            elif price > self.threshold:
                self.threshold_types.add(inst_type)

    def additional_instances_count(self, bound):
        return max(bound - len(self.running), 0)

    def add_instances(self, count, inst_type):
        for index in range(0, count):
            ec2 = EC2Facade(inst_type)
            self.running.append(ec2)

    def get_cheapest_type(self):
        items = self.prices.items()
        e = list(items)[0]
        k = e[0]
        v = e[1]
        for (key, value) in items:
            if (value < v):
                k = key
                v = value
        return (k, v)

    def remove_terminated(self):
        terminated_instances = list(filter(lambda x: x.get_status() == EC2Facade.TERMINATED, self.running))
        for instance in terminated_instances:
            self.running.remove(instance)

    def perform_maintenance(self):
        self.update_prices()
        self.stop_instances()
        self.terminate_instances()
        self.remove_terminated()
        self.create_optional_instances()

    def stop_instances(self):
        instances_to_stop = self.get_exceeding_threshold_instances()
        instances_to_stop_count = len(instances_to_stop)
        if instances_to_stop_count > 0:
            running_count = self.count_running_instances()
            if running_count > self.min_count:
                diff = running_count - self.min_count
                count_to_stop = min(diff, instances_to_stop_count)
                for instance in instances_to_stop[0: count_to_stop]:
                    instance.shutdown()

    def terminate_instances(self):
        instances = list(filter(lambda x: x.get_status() == EC2Facade.SHUTTING_DOWN and x.get_process_count() == 0, self.running))
        for instance in instances:
            instance.terminate()

    def count_running_instances(self):
        return len(list(filter(lambda x: x.get_status() == EC2Facade.RUNNING, self.running)))

    def get_exceeding_threshold_instances(self):
        return list(filter(lambda ins: ins.get_type() in self.threshold_types and ins.get_status() == EC2Facade.RUNNING, self.running))

    def report_status(self):
        print("\nstatus running instances")
        print("Running instances count: {}".format(self.count_running_instances()))
        prices = self.price_watcher.get_prices()
        for instance in self.running:
            id = instance.get_instance_id()
            inst_type = instance.get_type()
            price = prices[inst_type]
            status = instance.get_status()
            process_count = instance.get_process_count()
            above_threshold = price > self.threshold
            print("instance id: {}, status: {}, instance type: {}, price: {}, process count: {}, above threshold: {}".format(id, status, inst_type, price, process_count, above_threshold))