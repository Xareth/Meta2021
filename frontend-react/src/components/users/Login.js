import React, { useEffect } from "react";

function Login(props) {
    const menuItems = ["Login", "Users"]

    useEffect( () => {
        props.SetBottomMenu(menuItems)
        }, [])

    return <div>
        Login
    </div>
}

export default Login;