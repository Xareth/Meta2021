import React, { useEffect, useState } from "react";
import BottomMenu from "./layout/BottomMenu";
import SideMenu from "./layout/SideMenu";
import TopNavigation from "./layout/TopNavigation";

function App() {
    const [ isHidden, setHidden ] = useState(true);
    const [ sitelinksItems, setSiteLinksItems ] = useState("")
    const [ bottomMenuItems, setBottomMenuItems ] = useState([])

    useEffect(() => {
        fetch("/_get-all-users").then(response => response.json().then(data => {
            console.log(data);
        }))
    }, [])

    function SetHideSideMenu(event) {
        setHidden(!isHidden);
    }

    function SetSiteLinks(event) {
        console.log("nice");
    }

    function SetBottomMenu(event) {
        console.log("wow");
    }

    return <div className="container container-main">
        <TopNavigation
            SetHideSideMenu={SetHideSideMenu}
            sitelinksItems={sitelinksItems}
            setSiteLinks={SetSiteLinks}
        />
        <div className="container-content"></div>
        <BottomMenu
            setBottomMenu={SetBottomMenu}
            bottomMenuItems={bottomMenuItems}
        />
        <SideMenu
            SetHideSideMenu={SetHideSideMenu}
            isHidden={isHidden}
        />
    </div>
}

export default App;
