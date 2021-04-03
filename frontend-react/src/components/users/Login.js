import React, { useEffect } from "react";
import _LoginForm from "./_LoginForm";


function Login(props) {
    const menuItems = ["Login", "whatever"];

    // Create Bottom menu when page is called
    useEffect( () => {
        props.SetBottomMenu(menuItems);
        }, [])

    return <div>
        {props.subMod === "Login" ? <_LoginForm subMod={props.subMod} /> : ""}
    </div>
}


export default Login;