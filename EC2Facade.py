import random


class EC2Facade:
    """

    """
    RUNNING = "Running"
    SHUTTING_DOWN = "Shutting down"
    TERMINATED = "Terminated"

    id = 1

    def __init__(self, type, instance = None):
        self.type = type
        self.instance = instance
        self.status = EC2Facade.RUNNING
        self.instance_id = EC2Facade.id
        self.process_count = random.randrange(5)
        EC2Facade.id += 1

    def shutdown(self):
        """
        prepare instance to be closed
        Returns:

        """
        self.status = EC2Facade.SHUTTING_DOWN
        # self.instance.close()

    def get_instance_id(self):
        return self.instance_id

    def get_type(self):
        return self.type

    def get_status(self):
        return self.status

    def get_process_count(self):
        """

        Returns: Int

        """
        if self.status == EC2Facade.RUNNING:
            return random.randrange(10)
        elif self.status == EC2Facade.SHUTTING_DOWN and self.process_count > 0:
            self.process_count = random.randrange(self.process_count)
        else:
            return self.process_count

    def terminate(self):
        self.status = EC2Facade.TERMINATED

