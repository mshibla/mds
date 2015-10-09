This is mds, a metadata service for tracking and locating artifacts spread
across multiple artifact repositories of different types.  The stateful data
is stored in a mysql database (I used RDS with mysql in this proof-of-concept).
The database interface library uses sqlalchemy.  The executable (amdata) 
makes use of the database interface library to search and update the
artifact metadata.

Key considerations are:

 - artifact repositories are not guaranteed to be of the same technology,
 - an artifact name plus an artifact version uniquely identifies an artifact,
 - there may exist copies of artifacts in one or more repositories,
 - the metadata service must return a method of accessing an artifact (a URL)

