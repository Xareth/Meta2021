import React, {useState} from "react";
import Login from "./users/Login";
import Settings from "./settings/Settings";


function MainContent(props) {

    return <div id="main-content" className="container-content">
        {props.module === "login" ? <Login SetBottomMenu={props.SetBottomMenu} SubMod={props.subMod} /> : ""}
        {props.module === "settings" ? <Settings SetBottomMenu={props.SetBottomMenu} /> : ""}

    </div>
}

export default MainContent;