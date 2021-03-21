// import React, {useEffect, useState} from "react";
//
// function App() {
//
//     const [ users, setUsers ] = useState([])
//
//     useEffect(() => {
//         fetch("/_get-all-users").then(response => response.json().then(data => {
//             setUsers(data);
//             console.log(data);
//         }))
//     }, [])
//
//     function CreateUser(user) {
//         return <User
//             key={user.email}
//             email={user.email}
//         />
//     }
//
//     return (
//         <div>{users.map(CreateUser)}</div>
//     );
// }
//
// function User(props) {
//     return (<div>{props.email}</div>)
// }