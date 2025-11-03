#Computational Thinking Assignment 2 - User Login Notification System
import time #import time module for more detailed notifications
AUTHORIZED_USERS_LIST = [
    {
        'username': 'admin',
        'login_status': True,
        'account_role': 'admin',
        'subscription_type': 'Pro',
        'permissions': ['create_user', 'edit_content', 'view_reports']
    },
    {
        'username': 'editor1',
        'login_status': True,
        'account_role': 'editor',
        'subscription_type': 'Pro',
        'permissions': ['edit_content', 'view_reports']
    },
    {
        'username': 'viewer1',
        'login_status': True,
        'account_role': 'viewer',
        'subscription_type': 'Free',
        'permissions': ['view_reports']
    },
            {
        'username': 'viewer2',
        'login_status': False,
        'account_role': 'viewer',
        'subscription_type': 'Free',
        'permissions': ['view_reports']
    },
        {
        'username': 'viewer3',
        'login_status': False,
        'account_role': 'viewer',
        'subscription_type': 'Free',
        'permissions': ['view_reports']
    }
]

for user in AUTHORIZED_USERS_LIST: #for loop to check each user's login status
    if user['login_status']:
        print("-- User Login Detected --")
        print(f" Notifying User: {user['username']} with updated status.")
        print(f" Role: {user['account_role']}")
        print(f" Subscription: {user['subscription_type']}")
        print(f" Permissions: {user['permissions']}")
        print(f" Time of Notification & Check:", time.ctime())
        print("--------------------------")
    else:
        print("--------------------------")
        print(f"Skipping user: {user['username']} - user inactive, awaiting login.")
        print(f" Time of Notification & Check:", time.ctime())
        print("--------------------------")

print("End of user status checks.")