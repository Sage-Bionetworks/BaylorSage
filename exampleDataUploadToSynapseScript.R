require(synapseClient)
synapseLogin()


foo <- data.frame(a=rnorm(10),
                  b=rnorm(10),
                  c=rnorm(10),
                  stringsAsFactors = F)
View(foo)

write.table(foo,
          file='exampleData.csv',
          quote=F,
          row.names=F,
          sep=',')



###Create a new folder in the collaboration space
testFolderObj <- synapseClient::Folder(name='Test Data',
                                       parentId='syn7342718')

testFolderObj <- synapseClient::synStore(testFolderObj)

###Grab the Synapse Id of this new folder
folderId<- synapseClient::synGetProperty(testFolderObj,'id')


dataObj <- synapseClient::File(path = 'exampleData.csv',
                               parentId=folderId)

annos <- list(foo = 'bar',
              baz = 'bax',
              fileType = 'csv')


synapseClient::synSetAnnotations(dataObj) <- annos

require(githubr)



