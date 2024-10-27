# Crypto Lens 

Hackathon- Encode London <br/>
Track- Defi Data Analysis, Compass Labs Zone <br/>
Project link- https://cryptolens-encode.streamlit.app/Dashboard <br/>
Team members- Alexander Tallis, Anjani Upadhyay, Harold Robson, Niharika Deokar- University of Bristol
(The project screenshots have been added to the file- screenshots.md)

For our DeFi Data Analysis project- CryptoLens, we've been granted access to a subset of the "dojo" database, featuring curated and processed smart contract data. The data primarily consists of two types: Event Data, which refers to specific events emitted by the Ethereum Virtual Machine (EVM), which developers explicitly program into smart contracts to track important actions, and Call Data, which represents the outputs from function calls on smart contracts.

Using the data from Ethereum and Arbitrum transactions from June to September of 2024, we have performed several analyses to understand the discrepancies between the two tokens, and any interesting features of how they are traded. Our data first shows the distribution of different transaction types within each token. Whilst the majority of transaction types in both tokens are swapped, we can see that arbitrum has a much wider range of transaction types. Since the swaps are the dominant transaction method, we inspected the Ethereum swaps in more detail, creating a graph of the top Ethereum swap traders, and observing many connections between them as they trade with one another. We can see that those who trade the least are much more disconnected. This illustrates the increased networking between the biggest players in the market. We also created graphs displaying the net change in Ethereum and Arbitrum being minted/burnt over time in the market, this useful metric may be indicative of price due to supply and demand. The Ethereum showed a steady inflation, whilst the arbitrum was more volatile. 
<br/>
<br/>
Finally, we observed the net borrow/repay transactions in the market for Ethereum. This gives us an overall picture of market health, since as the price of a token goes down, people repay their loans more. We can observe this clearly with a big spike upwards in loan repayments when Ethereum crashed in early August. 
<br/>
This data has been displayed in the form of an interactive streamlit dashboard and an iOS app.


