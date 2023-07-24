# Connect to the WebLogic domain
connect()

# Print a blank line for better formatting
print ''

# Print a message to indicate that we are changing the password for a specific datasource
print '======================================================'
print 'Change Password for Datasource (myDataSource)'
print '======================================================'
print ''

# Start editing the domain configuration
edit()
startEdit()

# Navigate to the specific datasource configuration to change its password
cd('/JDBCSystemResources/myDataSource/JDBCResource/myDataSource/JDBCDriverParams/myDataSource')

# Set the new encrypted password for the datasource
set('PasswordEncrypted', '{AES256}Dn04cfUTAurjzqFi4i4xJCIb811sLXyCEamvOierBD0=')

# Activate the changes to make them effective
activate()
