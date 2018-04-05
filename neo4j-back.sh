file=`date '+%m%d%y-%H%M%S'`

echo 'Shut down Neo4j ...'
service neo4j stop

echo 'Start backup ...'
neo4j-admin dump --database=graph --to=/mnt/data/test/$file.cypher

echo 'Start Neo4j ...'
service neo4j start

echo 'zip the backup file'
tar -czvf /mnt/data/test/$file.tar.gz /mnt/data/test/$file.cypher

su - rt -c "scp /mnt/data/test/$file.tar.gz ubuntu@52.42.109.175:/var/www/html"

echo 'file transfer complete ...'

echo 'start transfering the backup file ...'
su - rt -c "scp /mnt/data/test/$file.tar.gz ubuntu@52.42.109.175:/var/www/html"



