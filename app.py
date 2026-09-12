import streamlit as st

st.set_page_config(page_title="Bharat Pay Bridge", page_icon="🌉")

st.title("🌉 Bharat Global Pay Bridge")
st.markdown("**Solving Cross-Border Payments for Sanctioned Countries | Built by Sai Srivardhan, Rajahmundry**")
st.divider()

country = st.text_input("🌍 Recipient Country - Enter Country Name", "Iran")

sanctioned_list = ["iran", "russia", "syria", "north korea", "cuba", "belarus", "venezuela"]

if country:
    if country.lower() in sanctioned_list:
        st.error(f"🚫 PAYMENT BLOCKED DUE TO SANCTIONS to {country.upper()}")
        st.write("Direct bank transfer is blocked due to OFAC/SWIFT sanctions.")
        
        st.success("✅ **Legal Mobile Money Bridge - Compliant Solution Available**")
        c1, c2 = st.columns(2)
        c1.metric("Our Fee", "2%", "-6% vs Banks")
        c2.metric("Transfer Time", "5 Mins", "Fast")
        
        st.info("How? Via licensed mobile wallets + RBI approved partner corridor. 100% Legal.")
        
        if st.button("🔒 Proceed via Legal Bridge (DEMO)", type="primary"):
            st.balloons()
            st.success("SUCCESS! Transfer Initiated\n\nAmount: ₹10,000\nFee: ₹200\nTotal: ₹10,200")
    else:
        st.success(f"✅ Payment to {country} is ALLOWED via SWIFT banking - No restrictions.")

st.divider()
st.caption("Tech: Python + Streamlit | For Job Portfolio | Contact: LinkedIn")