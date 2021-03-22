import React, { useState } from "react";

function SideMenu(props) {

    const [ sitelinksItems, setSiteLinksItems ] = useState([{"name": "Salon nowe", "route": "salon-nowe"},
        {"name": "Salon używane", "route": "salon-uzywane"}, {"name": "Ustawienia", "route": "ustawienia"}])

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