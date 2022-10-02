function Header()
{
    return (
        <div>
            <div className="landingPageFlexBox">
                <img className="landingPageLogo" src="src/UMBCLogo.png"></img>
                <h1 className="landingPageTitle">GritMeals</h1>          
            </div>

            <p className="landingPageDescription">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu placerat lorem. Ut diam lorem, Nunc tempus, lectus quis ultricies sodales, ex sapien pellentesque libero, congue ullamcorper augue nibh ac eros.</p>
        </div>
    )
}

function EmailBox()
{
    return (
        <div>
            <input class="landingPageEmailBox" id="emailInput" type="email" placeholder="Your Email Address"></input>   
        </div>
    )
}

function Buttons()
{
    return (
        <div>
            <button className="landingButtons" onClick={signIn}>GET STARTED</button>
        </div>
    )
}


function SideBar()
{
    return (
        <div className="landingPageSideBar">
        </div>
    )    
}


function LeftColumn()
{
    return(
        <div>
            <Header />
            <EmailBox />    
            <Buttons />
        </div>
    )
}



function RightColumn()
{
    return (
        <div className="landingPageInfoColumn">
            <h1>A sentence goes here 1</h1>
            <h1>A sentence goes here 2</h1>
            <h1>A sentence goes here 3</h1>
            <h1>A sentence goes here 4</h1>
            <h1>A sentence goes here 5</h1>
        </div>  
    )
}


function MainContent()
{
    return (
        <div className="landingPageContentDivider">
            <LeftColumn />
            <RightColumn />
        </div>
    )

}

ReactDOM.render(<MainContent />, document.getElementById("root"))



//
function signIn()
{
    var content = document.getElementById("emailInput").value
    alert(content)
}