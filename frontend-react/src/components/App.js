import React, { useEffect, useState } from "react";
import BottomMenu from "./layout/BottomMenu";
import SideMenu from "./layout/SideMenu";
import TopNavigation from "./layout/TopNavigation";
import MainContent from "./MainContent";

function App() {
    const [ isHidden, setHidden ] = useState(true);
    const [ bottomMenuItems, setBottomMenuItems ] = useState([])
    const [ module, setModule ] = useState("login")

    // to delete
    useEffect(() => {
        fetch("/login").then(response => response.json().then(data => {
            console.log(data);
        }))
    }, [])

    // Hides side menu
    function SetHideSideMenu(event) {
        setHidden(!isHidden);
    }

    // Generates items in bottom menu
    function SetBottomMenu(event) {
        console.log(event);
        setBottomMenuItems(event);
    }

    // Sets name of current module
    function SetModuleName(event) {
        console.log(event.target.attributes[0].nodeValue);
        setModule(event.target.attributes[0].nodeValue);
    }

    // Renders 4 main website components
    return <div className="container container-main">
        <TopNavigation
            SetHideSideMenu={SetHideSideMenu}
        />
        <MainContent
            SetBottomMenu={SetBottomMenu}
            module={module}
        />
        <BottomMenu
            bottomMenuItems={bottomMenuItems}
        />
        <SideMenu
            SetHideSideMenu={SetHideSideMenu}
            SetModuleName={SetModuleName}
            isHidden={isHidden}
        />
    </div>
}

export default App;
