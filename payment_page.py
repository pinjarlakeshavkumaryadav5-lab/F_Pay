import React, { useState } from "react";
import "./Payment.css";

function PaymentPage() {

const [paymentMethod,setPaymentMethod]=useState("");

const payNow=()=>{

if(paymentMethod===""){

alert("Please Select Payment Method");

return;

}

alert("Redirecting To OTP Verification...");

}

return(

<div className="paymentContainer">

<h1>F Pay</h1>

<div className="paymentCard">

<h2>Fee Payment</h2>

<input
type="text"
value="22081A66G1"
readOnly
placeholder="Admission Number"
/>

<input
type="text"
value="IV B.Tech AIML"
readOnly
placeholder="Class"
/>

<input
type="text"
value="₹25,000"
readOnly
placeholder="Fee Amount"
/>

<h3>Select Payment Method</h3>

<label>

<input
type="radio"
name="payment"
value="UPI"
onChange={(e)=>setPaymentMethod(e.target.value)}
/>

UPI

</label>

<label>

<input
type="radio"
name="payment"
value="Debit Card"
onChange={(e)=>setPaymentMethod(e.target.value)}
/>

Debit Card

</label>

<label>

<input
type="radio"
name="payment"
value="Credit Card"
onChange={(e)=>setPaymentMethod(e.target.value)}
/>

Credit Card

</label>

<label>

<input
type="radio"
name="payment"
value="Net Banking"
onChange={(e)=>setPaymentMethod(e.target.value)}
/>

Net Banking

</label>

<input
type="text"
placeholder="Card Holder Name"
/>

<input
type="text"
placeholder="Card Number"
/>

<div className="row">

<input
type="text"
placeholder="MM/YY"
/>

<input
type="password"
placeholder="CVV"
/>

</div>

<button
className="payButton"
onClick={payNow}
>

Pay ₹25,000

</button>

</div>

</div>

);

}

export default PaymentPage;
