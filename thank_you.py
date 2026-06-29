import React from "react";
import { useNavigate } from "react-router-dom";
import "./ThankYou.css";

function ThankYouPage() {

const navigate = useNavigate();

const paymentID =
"FPAY"+Math.floor(Math.random()*1000000);

return(

<div className="thankContainer">

<div className="thankCard">

<div className="tick">

✔

</div>

<h1>

Payment Successful

</h1>

<h2>

Thank You For Successful Payment

</h2>

<p>

Your Fee Payment has been completed successfully.

</p>

<div className="receipt">

<h3>Receipt Details</h3>

<p>

Payment ID :

<strong>

{paymentID}

</strong>

</p>

<p>

Amount :

<strong>

₹25,000

</strong>

</p>

<p>

Status :

<strong className="success">

SUCCESS

</strong>

</p>

</div>

<button className="download">

Download Receipt

</button>

<button

className="dashboard"

onClick={()=>navigate("/dashboard")}

>

Go To Dashboard

</button>

</div>

</div>

);

}

export default ThankYouPage;
