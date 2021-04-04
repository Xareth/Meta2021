import React, {useState} from "react";
import Login from "./users/Login";
import Settings from "./settings/Settings";


function MainContent(props) {

    return <div id="main-content" onClick={props.SetCloseSideMenu} className="container-content">
        {props.module === "login" ? <Login SetBottomMenu={props.SetBottomMenu} subMod={props.subMod}
                                           SetSubMod={props.SetSubMod} /> : ""}
        {props.module === "settings" ? <Settings SetBottomMenu={props.SetBottomMenu} subMod={props.subMod}
                                                 SetSubMod={props.SetSubMod} /> : ""}
    </div>
}

export default MainContent;