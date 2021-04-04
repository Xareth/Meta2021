import React, { useEffect, useState } from "react";
import RenderForm from "../forms/FormHandler";


function _LoginForm(props) {

    const [ loginForm, setLoginForm ] = useState([]);
    const methods = {
        "setSubMod": props.setSubMod,
        "route": "/_login"
    }

    // Render form
    return RenderForm(loginForm, setLoginForm, methods)
}


export default _LoginForm;