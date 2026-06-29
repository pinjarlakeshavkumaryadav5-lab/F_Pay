import React, { useState } from "react";
import "./Login.css";

function LoginPage() {

const [studentName,setStudentName]=useState("");
const [admissionNumber,setAdmissionNumber]=useState("");
const [password,setPassword]=useState("");
const [showPassword,setShowPassword]=useState(false);

const login=()=>{

if(
studentName===""||
admissionNumber===""||
password==="")
{

alert("Please Fill All Fields");

return;

}

alert("Login Successful");

}

return(

<div className="login-container">

<h1>F Pay</h1>

<input
type="text"
placeholder="Student Name"
value={studentName}
onChange={(e)=>setStudentName(e.target.value)}
/>

<input
type="text"
placeholder="Admission Number"
value={admissionNumber}
onChange={(e)=>setAdmissionNumber(e.target.value)}
/>

<input
type={showPassword?"text":"password"}
placeholder="Password"
value={password}
onChange={(e)=>setPassword(e.target.value)}
/>

<div className="showPassword">

<input
type="checkbox"
onChange={()=>setShowPassword(!showPassword)}
/>

Show Password

</div>

<p className="forgot">

Forgot Password?

</p>

<button
className="submitButton"
onClick={login}
>

Submit

</button>

</div>

);

}

export default LoginPage;
