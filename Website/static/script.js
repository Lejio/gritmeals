function Header()
{
    return (
        <div>
            <div className="landingPageFlexBox">
                <img className="landingPageLogo" src="src/UMBCLogo.png"></img>
                <h1 className="landingPageTitle">GritMeals</h1>          
            </div>

            <p className="landingPageDescription">GritMeals is a quality-of-life service that automatically curates and displays dining information from True Grits.</p>
            <p className="getStartedText">To get started, simply enter your email address:</p>        
        </div>
    )
}

function Footer()
{
    return (
        <div className="footer">
            <h1>A hackUMBC project written by Ahmad Sayad, Gene Ni, & Pranav Senthilvel.</h1>
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
            <Footer />
        </div>
    )
}

function InfoContent()
{
    return(
        <div>
            <h1 className="infoContentTitle">How GritMeals Works</h1>
            
            <div className="infoContent">
                <h2>GritMeals was built using numerous technologies, including React, Mailchimp, Flask, SQLite, nginx, and Google Computing Engine.</h2>
                <h2>GritMeals does four things when you enter your email address:</h2> 

                <ol className="infoList">
                    <li className="infoListItem"> Your email address is stored into a mailing database to recieve daily dining updates. </li>
                    <li className="infoListItem"> GritMeals searches through and curates dining information from True Grits using a Chartwells API.</li>
                    <li className="infoListItem"> The curated dining information is then formatted into an interactive HTML-embedded email. </li>                
                    <li className="infoListItem"> The HTML-embedded email is then sent to all registered users at 6:00 AM (EST). </li>
                </ol>

                <a className="githubLink" href="https://github.com/Lejio/gritmeals">
                    <h1 className="githubLinkText">Visit our GitHub!</h1>
                </a>
            </div>
        </div>
    )
}


function RightColumn()
{
    return (
        <div className="landingPageInfoColumn">
            <InfoContent />
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
    
    if (content != "")
    {
        alert(content)
    }
}