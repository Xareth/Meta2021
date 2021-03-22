import React, { useState } from "react";

function SideMenu(props) {

    const [ sitelinksItems, setSiteLinksItems ] = useState([
        {"name": "login", "route": "login"},
        {"name": "ustawienia", "route": "settings"}
        ])

    function SetSiteLinks(event) {
        console.log("nice");
    }

    return (<div className={props.isHidden ? "sideMenu sideMenu-hidden" : "sideMenu"}>
        <div className="sideMenu-close" onClick={props.SetHideSideMenu}><i className="fas fa-times"></i></div>
        <div className="sideMenu-moduls">
            <ul>
                {sitelinksItems.map((data) => {
                    return (<SiteItem
                        key={data.name}
                        name={data.name}
                        route={data.route}
                        setModuleName={props.SetModuleName}
                    />)
                })}
            </ul>
        </div>
    </div>)
}


function SiteItem(props) {
    return <li name={props.route} onClick={props.setModuleName}>{props.name}</li>
}

export default SideMenu;