(this["webpackJsonpfrontend-react"]=this["webpackJsonpfrontend-react"]||[]).push([[0],{10:function(e,t,n){},12:function(e,t,n){"use strict";n.r(t);var s=n(1),c=n.n(s),o=n(4),i=n.n(o),a=(n(9),n(10),n(2)),u=n(0);function r(e){return Object(u.jsx)(j,{name:e},e)}function j(e){return Object(u.jsx)("button",{className:"button btn-botMenu",children:e.name})}var l=function(e){return Object(u.jsx)("div",{className:"bottomMenu",children:e.bottomMenuItems.map(r)})};function d(e){return Object(u.jsx)("li",{name:e.route,onClick:e.setModuleName,children:e.name})}var b=function(e){var t=Object(s.useState)([{name:"Salon nowe",route:"salon-nowe"},{name:"Salon u\u017cywane",route:"salon-uzywane"},{name:"Ustawienia",route:"ustawienia"}]),n=Object(a.a)(t,2),c=n[0];return n[1],Object(u.jsxs)("div",{className:e.isHidden?"sideMenu sideMenu-hidden":"sideMenu",children:[Object(u.jsx)("div",{className:"sideMenu-close",onClick:e.SetHideSideMenu,children:Object(u.jsx)("i",{className:"fas fa-times"})}),Object(u.jsx)("div",{className:"sideMenu-moduls",children:Object(u.jsx)("ul",{children:c.map((function(t){return Object(u.jsx)(d,{name:t.name,route:t.route,setModuleName:e.SetModuleName},t.name)}))})})]})};var m=function(e){return Object(u.jsxs)("div",{className:"topNavigation",children:[Object(u.jsx)("div",{className:"tn-right",children:Object(u.jsx)("p",{onClick:e.SetHideSideMenu,children:Object(u.jsx)("i",{className:"fas fa-bars"})})}),Object(u.jsx)("div",{className:"tn-logo",children:Object(u.jsx)("div",{children:Object(u.jsx)("img",{src:"static/base/MotortestLogoPoziome.png",alt:"logo"})})}),Object(u.jsxs)("div",{className:"tn-mid",children:[Object(u.jsxs)("div",{className:"tn-mid-long",children:[Object(u.jsx)("span",{children:" Home "}),Object(u.jsx)("i",{className:"fas fa-angle-right"}),Object(u.jsx)("span",{children:" Settings "}),Object(u.jsx)("i",{className:"fas fa-angle-right"}),Object(u.jsx)("span",{children:" Roles "})]}),Object(u.jsx)("div",{className:"tn-mid-short",children:Object(u.jsx)("span",{children:" Roles "})})]})]})};var O=function(e){var t=["Login","Users"];return Object(s.useEffect)((function(){e.SetBottomMenu(t)}),[]),Object(u.jsx)("div",{children:"Login"})};var f=function(e){var t=["Set","Ings"];return Object(s.useEffect)((function(){e.SetBottomMenu(t)}),[]),Object(u.jsx)("div",{children:"Login"})};var x=function(e){return Object(u.jsxs)("div",{className:"container-content",children:["login"===e.module?Object(u.jsx)(O,{SetBottomMenu:e.SetBottomMenu}):"","salon-nowe"===e.module?Object(u.jsx)(f,{SetBottomMenu:e.SetBottomMenu}):"","salon-uzywane"===e.module?Object(u.jsx)(O,{SetBottomMenu:e.SetBottomMenu}):""]})};var h=function(){var e=Object(s.useState)(!0),t=Object(a.a)(e,2),n=t[0],c=t[1],o=Object(s.useState)([]),i=Object(a.a)(o,2),r=i[0],j=i[1],d=Object(s.useState)("login"),O=Object(a.a)(d,2),f=O[0],h=O[1];function v(e){c(!n)}return Object(s.useEffect)((function(){fetch("/login").then((function(e){return e.json().then((function(e){console.log(e)}))}))}),[]),Object(u.jsxs)("div",{className:"container container-main",children:[Object(u.jsx)(m,{SetHideSideMenu:v}),Object(u.jsx)(x,{SetBottomMenu:function(e){console.log(e),j(e)},module:f}),Object(u.jsx)(l,{bottomMenuItems:r}),Object(u.jsx)(b,{SetHideSideMenu:v,SetModuleName:function(e){console.log(e.target.attributes[0].nodeValue),h(e.target.attributes[0].nodeValue)},isHidden:n})]})};i.a.render(Object(u.jsx)(c.a.StrictMode,{children:Object(u.jsx)(h,{})}),document.getElementById("root"))},9:function(e,t,n){}},[[12,1,2]]]);
//# sourceMappingURL=main.0ec0c03a.chunk.js.map