import React, { useEffect } from "react";
import _LoginForm from "./_LoginForm";


function Login(props) {
    const menuItems = ["Login", "whatever"];

    // Create Bottom menu when page is called
    useEffect( () => {
        props.SetBottomMenu(menuItems);
        fetch("/_users").then(response => response.json().then(data => {
            console.log(data);
        })).catch((e) => { console.log("Error occured: ",e) })
        }, [])

    return <div>
        {props.subMod === "Login" ? <_LoginForm /> : ""}
    </div>
}

export default Login;