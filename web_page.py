import React from "react";
import "./Dashboard.css";

function Dashboard() {

return(

<div className="dashboard">

<header className="header">

<h1>F Pay</h1>

<button className="logout">

Logout

</button>

</header>

<div className="profileCard">

<img
src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
alt="Student"
/>

<h2>Keshav Kumar Yadav</h2>

<p>Admission No : 22081A66G1</p>

<p>Institution : Swami Vivekananda Institute Of Technology</p>

<p>Class : IV B.Tech AIML</p>

</div>

<div className="feeCard">

<h2>Student Fee Details</h2>

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
value="Telangana"
readOnly
placeholder="State"
/>

<input
type="text"
value="Hyderabad"
readOnly
placeholder="City"
/>

<input
type="text"
value="500090"
readOnly
placeholder="Postal Code"
/>

<input
type="text"
value="₹ 25,000"
readOnly
placeholder="Fee Amount"
/>

<button className="payButton">

Pay Fee

</button>

</div>

<div className="history">

<h2>Transaction History</h2>

<table>

<thead>

<tr>

<th>Date</th>

<th>Amount</th>

<th>Status</th>

</tr>

</thead>

<tbody>

<tr>

<td>15/06/2026</td>

<td>₹15,000</td>

<td>Paid</td>

</tr>

<tr>

<td>20/07/2026</td>

<td>₹10,000</td>

<td>Pending</td>

</tr>

</tbody>

</table>

</div>

</div>

);

}

export default Dashboard;
