import urllib
import json
import server


testedServer = server.Server()
rescuers=server.all_rescuers()
assert (len(rescuers) == 2)
expected_rescuer1={'latitude': 32.2, 'last_update_time': '2012-12-01T06:00:00Z', 'phone_number': '052-6666666', 'rank': 'the best', 'longitude': 34.2}
expected_rescuer2={'latitude': 31.2, 'last_update_time': '2012-12-05T06:00:00Z', 'phone_number': '052-6666667', 'rank': 'jack the ripper', 'longitude': 37.2}

assert (expected_rescuer1 == rescuers[0])
assert (expected_rescuer2 == rescuers[1])
