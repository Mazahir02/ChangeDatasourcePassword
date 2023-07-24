# Prompt user to enter the new database password
DBPASSWORD = raw_input("Enter new DBPASSWORD:")

# Specify the path of the WebLogic domain
DOMAIN_PATH = '/u02/oracle/Oracle/Middleware/Oracle_Home/domains/fmw_domain'

# The name of the datasource to update
DS_NAME = 'myDataSource'

# Encrypt the entered password using the encrypt() function
es = encrypt(DBPASSWORD, DOMAIN_PATH)

# Connect to the WebLogic domain
connect()

# Start editing the domain configuration
edit()
startEdit()

# Navigate to the JDBCSystemResources to get all datasources
cd('JDBCSystemResources')
allDS = cmo.getJDBCSystemResources()

# Loop through all datasources and find the specified DS_NAME
for tmpDS in allDS:
    dsName = tmpDS.getName()
    if dsName == DS_NAME:
        # If DS_NAME matches, change the password for the datasource
        print 'Changing the Password for DataSource ', dsName
        cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName)
        set('PasswordEncrypted', es)

# Save the changes made to the configuration
save()

# Activate the changes to make them effective
activate()

# Disconnect from the WebLogic domain
disconnect()
