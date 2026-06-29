import React, { useState } from "react";
import "./Registration.css";

function RegistrationPage() {

const [studentName, setStudentName] = useState("");
const [dob, setDob] = useState("");
const [admissionNo, setAdmissionNo] = useState("");
const [institution, setInstitution] = useState("");
const [studentClass, setStudentClass] = useState("");
const [parentName, setParentName] = useState("");

const registerStudent = () => {

if(
studentName===""||
dob===""||
admissionNo===""||
institution===""||
studentClass===""||
parentName==="")
{

alert("Please Fill All Fields");

return;

}

alert("Registration Successful");

}

return(

<div className="register-page">

<h1>F Pay</h1>

<p className="already">

Already Registered?

<button className="login">

Login

</button>

</p>

<input
type="text"
placeholder="Student Name"
value={studentName}
onChange={(e)=>setStudentName(e.target.value)}
/>

<input
type="date"
value={dob}
onChange={(e)=>setDob(e.target.value)}
/>

<input
type="text"
placeholder="Admission Number"
value={admissionNo}
onChange={(e)=>setAdmissionNo(e.target.value)}
/>

<input
type="text"
placeholder="Institution Name"
value={institution}
onChange={(e)=>setInstitution(e.target.value)}
/>

<input
type="text"
placeholder="Class"
value={studentClass}
onChange={(e)=>setStudentClass(e.target.value)}
/>

<input
type="text"
placeholder="Parent Name"
value={parentName}
onChange={(e)=>setParentName(e.target.value)}
/>

<button
className="registerButton"
onClick={registerStudent}
>

Register

</button>

</div>

);

}

export default RegistrationPage;
