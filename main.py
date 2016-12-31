import time
import InstanceTypes
from EC2Manager import EC2Manager
from PriceWatcher import PriceWatcher

if __name__ == "__main__":
    prices1 = {InstanceTypes.InstanceTypes.M4_LARGE: 11.0, InstanceTypes.InstanceTypes.XLARGE: 7.0,
               InstanceTypes.InstanceTypes.XLARGE_2: 6.0}
    prices2 = {InstanceTypes.InstanceTypes.M4_LARGE: 1.0, InstanceTypes.InstanceTypes.XLARGE: 7.0,
               InstanceTypes.InstanceTypes.XLARGE_2: 8.0}
    prices3 = {InstanceTypes.InstanceTypes.M4_LARGE: 11.0, InstanceTypes.InstanceTypes.XLARGE: 4.0,
               InstanceTypes.InstanceTypes.XLARGE_2: 16.0}
    prices4 = {InstanceTypes.InstanceTypes.M4_LARGE: 11.0, InstanceTypes.InstanceTypes.XLARGE: 7.0,
               InstanceTypes.InstanceTypes.XLARGE_2: 3.0}

    price_watcher = PriceWatcher(prices1)
    manager = EC2Manager(10, 5, 3, 10, price_watcher)
    price_watcher.set_prices(prices2)
    manager.report_status()
    time.sleep(2)
    manager.perform_maintenance()
    manager.report_status()
    time.sleep(2)
    price_watcher.set_prices(prices2)
    manager.perform_maintenance()
    manager.report_status()
    time.sleep(2)
    price_watcher.set_prices(prices4)
    manager.perform_maintenance()
    manager.report_status()
    time.sleep(2)
    price_watcher.set_prices(prices1)
    manager.perform_maintenance()
    manager.report_status()
    time.sleep(2)
    price_watcher.set_prices(prices3)
    manager.perform_maintenance()
    manager.report_status()
    time.sleep(2)
    price_watcher.set_prices(prices3)
    manager.perform_maintenance()
    manager.report_status()
    time.sleep(2)
    price_watcher.set_prices(prices3)
    manager.perform_maintenance()
    manager.report_status()
    time.sleep(2)
    price_watcher.set_prices(prices3)
    manager.perform_maintenance()
    manager.report_status()
    time.sleep(2)
    price_watcher.set_prices(prices3)
    manager.perform_maintenance()
    manager.report_status()
    time.sleep(2)
    price_watcher.set_prices(prices3)
    manager.perform_maintenance()
    manager.report_status()