 # Dchain
A election app on blockchain for codefundo++ 2019

 ## Usage

There are 3 roles assigned in the logic of the solidity smart contract
<ol>
<li>Admin(or Govt.)</li>
<li>Candidate </li>
<li>Voter </li>
<li>Candidates start registering to Election using Web UI which submits form to local database </li>
 <li>Admin is the person (or Government) who verifies application from candidates who are added to smart contract using azure blockchain workbench api</li>
 <li>Candidates upload there promises etc to the site and using ipfs api files are uploaded to IPFS public gateway </li>
 <li>Voters submit there proof of authority to the web UI which are then verified by admin and get voter id's issued </li>
 <li>Admin issues voter ids to voter ( Ethereum addresses which are stored in Azure Key Vault) based on proof of authority acquired from Govt database and adds them to the blockchain network using workbench api</li>
 <li> Voters then use the ids and choose candidates on the basis of there promises and vote there choice which is then sent to the smart contract using workbench api </li>
 <li> The smart contract keeps the count of votes to each candidate which are immutable due to use of Azure Blockchain Workbench and Ethereum </li>
 <li> Finally after the polling ends the results are casted publically to the site </li>
</ol>
  
 ## Technologies

<ol>
 <li>Azure Blockchain Workbench(For Deploying Smart Contract)</li>
 <li>Solidity Programing Language(For Smart Contract)</li>
  <li>Inter Planetary File System (for storing files) </li>
 <li>Django Web Framework(For User Interface)</li>
 <li>MySQL DB for database</li>
</ol>

