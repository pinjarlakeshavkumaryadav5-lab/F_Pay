import React, { useState } from "react";
import "./OTP.css";

function OTPPage() {

const [otp,setOtp]=useState(["","","","","",""]);

const handleChange=(value,index)=>{

if(value.length>1) return;

const newOtp=[...otp];

newOtp[index]=value;

setOtp(newOtp);

if(value!=="" && index<5){

document.getElementById(`otp-${index+1}`)?.focus();

}

}

const verifyOTP=()=>{

if(otp.join("").length!==6){

alert("Please Enter Valid OTP");

return;

}

alert("Payment Successful");

}

return(

<div className="otpContainer">

<div className="otpCard">

<h1>F Pay</h1>

<h2>OTP Verification</h2>

<p>

Enter the 6 Digit OTP sent to your registered mobile number.

</p>

<div className="otpBoxes">

{

otp.map((digit,index)=>(

<input

key={index}

id={`otp-${index}`}

type="text"

maxLength={1}

value={digit}

onChange={(e)=>handleChange(e.target.value,index)}

/>

))

}

</div>

<p className="timer">

OTP Expires In : 01:30

</p>

<button className="verifyBtn" onClick={verifyOTP}>

Verify Payment

</button>

<button className="resendBtn">

Resend OTP

</button>

</div>

</div>

);

}

export default OTPPage;
