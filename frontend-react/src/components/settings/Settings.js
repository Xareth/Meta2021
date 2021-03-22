import React, { useEffect } from "react";

function Settings(props) {
    const menuItems = ["Set", "Ings"]

    useEffect( () => {
        props.SetBottomMenu(menuItems)
    }, [])

    return <div>
        Login
    </div>
}

export default Settings;