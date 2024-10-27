
import streamlit as st

st.set_page_config(
    page_title="Introduction",
    page_icon="👋",
)

#this is done to hide the "made with streamlit" footer
hide_st_style="""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

zscore=0
st.markdown("## DeFi Data Analysis")
st.write("`Team members: Alex, Anjani, Harold, Niharika, Pakkanut- University of Bristol`")
st.write("##### DeFi")
with st.expander("**Explanation**"):
    st.write("Decentralized Finance, or DeFi, is an ecosystem of financial applications built on blockchain networks, especially Ethereum, that aims to recreate traditional financial systems—like lending, borrowing, and trading—using decentralized technologies. DeFi operates without centralized intermediaries like banks or brokerages, instead relying on smart contracts—self-executing contracts written in code on the blockchain that automatically carry out transactions when conditions are met.")

with st.expander("**Usage**"):
    st.write("DeFi analysis uses the transparency of DeFi protocols to help with data discovery, risk management, and financial opportunity decision-making.")
    st.write("Peer-to-peer trading-- DeFi exchanges use smart contracts to facilitate the trading of cryptocurrencies and tokens between two parties") 
    st.write("Lending and borrowing-- DeFi platforms allow users to lend or borrow cryptocurrencies without going through traditional financial institutions.")

st.write("DeFi has revolutionized access to financial services, allowing users to earn interest, trade assets, and access loans without intermediaries, expanding financial access and control for a global audience.")

st.divider()

st.write("##### Problem Statement")
st.write("Dive into DeFi database and analyse data from Uniswap, Aave, and GMX on Ethereum and Arbitrum. Goal is to uncover patterns and trends in the data.")

st.write("##### Data")
st.write("For our DeFi Data Analysis project, we've been granted access to a subset of the dojo database, featuring curated and processed smart contract data. The data primarily consists of two types:")

col1, col2= st.columns(2)

with col1:
    with st.expander("Event data"):
        st.write("This refers to specific events emitted by the Ethereum Virtual Machine (EVM), which developers explicitly program into smart contracts to track important actions. For example, a Uniswap v3 pool contract might emit events to log changes in token reserves or liquidity.")

with col2:
    with st.expander("Call data"):
        st.write("This data represents the outputs from function calls on smart contracts. For instance, in AAVE v3, calling a function like ⁠ getAssetPrice ⁠ will return the latest oracle-based price of a specific asset.")
        

st.write("Our hackathon database includes the following key tables: <br>•⁠  ⁠*hackathon_arbitrum_events*: Contains event data specific to the Arbitrum network. <br>•⁠  ⁠*hackathon_ethereum_call_data*: Holds call data from Ethereum smart contracts. <br>•⁠  ⁠*hackathon_ethereum_events*: Stores Ethereum-specific event data.", unsafe_allow_html=True)

st.divider()

st.write("##### Cryptocurrency")

with st.expander("**Explanation**"):
    st.write("Cryptocurrency is a digital or virtual form of currency that relies on cryptographic technology to secure transactions, control the creation of new units, and verify asset transfers. Unlike traditional currencies issued by governments (like dollars or euros), cryptocurrencies are typically decentralized, meaning they operate on a distributed ledger system, most commonly a blockchain.")

with st.expander("**Characteristics**"):
    st.markdown("- S⁠ecurity and Transparency")
    st.markdown("- Limited Supply")
    st.markdown("- Pseudonymity")
    st.markdown("- Smart Contracts")

st.write("The two cryptocurrencies analysed in this project are: Ethereum and Arbitrum")

text1 = """
<div style="background-color: #272730; padding: 14px; border-radius: 5px;">
    <p style="color: white; font-size: 15px;">Ethereum is a decentralized, open-source blockchain that enables smart contracts and decentralized applications (dApps). Created by Vitalik Buterin and launched in 2015, Ethereum was the first blockchain platform to introduce programmable contracts, which has driven the growth of DeFi, NFTs, and other decentralized solutions.
</p>
</div>
"""

text2 = """
<div style="background-color: #272730; padding: 14px; border-radius: 5px;">
    <p style="color: white; font-size: 15px;">Arbitrum is a Layer 2 scaling solution built on top of Ethereum, designed to improve transaction speed and lower costs by processing transactions off the main Ethereum chain. Arbitrum was created by Offchain Labs and launched in 2021. It is an Optimistic Rollup, a type of technology that batches multiple transactions and submits them to Ethereum as a single transaction, thereby reducing congestion and gas fees on the Ethereum network.
</p>
</div>
"""

col1, col2= st.columns(2)
with col1: 
    st.markdown(text1, unsafe_allow_html=True)

with col2: 
    st.markdown(text2, unsafe_allow_html=True)


#-------------------------------
    
