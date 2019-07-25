import sys
sys.path.insert(0, '../')
import helpers
from tqdm import tqdm
def removeUsers(activeUsers,allUsers):
	# removes all active users from the total user pool
	k = 0
	print("removing active users from userbase")
	for i in range(0,len(activeUsers)):
		for j in range(0,len(allUsers)):
			if allUsers[j-k]['ID'] == activeUsers[i]['ID']:
				print("found match of: ",allUsers[j-k]['ID'], activeUsers[i]['ID'])
				del allUsers[j-k]
				k += 1
	return allUsers


def main():
	activeUsersPath = "../active_users.csv"
	allUsersPath = "../comprehensive_user_data.csv"
	activeUsers = helpers.openCSVdict(activeUsersPath)
	allUsers = helpers.openCSVdict(allUsersPath)
	print("len of all users: ",len(allUsers))

	remainingUsers = removeUsers(activeUsers,allUsers)

	helpers.writeCSV(remainingUsers,"emailMe.csv",["NAME","EMAIL"])

main()