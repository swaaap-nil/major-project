import { Box, CssBaseline, TextField, Paper, Button, List, ListItem, ListItemText } from "@mui/material";
import AppTheme from "../shared-theme/AppTheme";
import SideMenu from "../dashboard/components/SideMenu";
import AppNavbar from "../dashboard/components/AppNavbar";
import { useState } from "react";
import AutoAwesomeIcon from '@mui/icons-material/AutoAwesome';
import Header from "../dashboard/components/Header";
import { height } from "@mui/system";

export default function Model(props: { disableCustomTheme?: boolean }) {
  const [essayText, setEssayText] = useState("");
  const [htmlContent, setHtmlContent] = useState("");

  const handleSampleTextClick = (sampleText: string) => {
    setEssayText(sampleText);
  };

  const handleIdentifySkillsClick = async () => {
    try {
        const response = await fetch(`http://localhost:8000/extract-skills-html/?job_description=${essayText}`, {
          method: "GET", // Use GET method as we're passing data in the URL
          headers: {
            "Content-Type": "application/json",
          },
        });
      if (response.ok) {
        const responseText :any= await response.json(); // Assuming the response is HTML
        console.log(responseText)
        setHtmlContent(responseText.data); // Set the HTML content received from the backend
      } else {
        console.error("Failed to fetch HTML content");
      }
    } catch (error) {
      console.error("Error during fetch:", error);
    }
  };

  return (
    <AppTheme {...props}>
      <CssBaseline enableColorScheme />
      <Box sx={{ display: 'flex' }}>
        <SideMenu />
        <AppNavbar />
        
        <Box sx={{height:'100vh'}}>
          {/* <Header path={['Dashboard','Home']}/> */}
          </Box>
          {/* Left Section */}
        <Box
        component="main"
          sx={{
            width: '50%',
            display: 'flex',
            flexDirection: 'column',
            mt:2,
            padding: 2,
            gap: 2
            
          }}
        >
          {/* Essay Input Section - 50% of left half */}
          <Box sx={{ height: '50%' }}>
            <TextField
              label="Provide a Job Description"
              multiline
              fullWidth
              variant="outlined"
              value={essayText}
              onChange={(e) => setEssayText(e.target.value)}
              sx={{
                height: 'calc(100% - 48px)', // Subtract button height + margin
                '& .MuiInputBase-root': {
                  height: '100%',
                },
                '& .MuiInputBase-input': {
                  height: '100% !important',
                  alignItems: 'flex-start !important',
                  verticalAlign: 'top',
                  overflowY: 'auto !important'
                }
              }}
            />
            <Button 
              variant="contained" 
              color="primary"
              sx={{ mt: 1.5, display: 'block', mx: 'auto' }}
              onClick={handleIdentifySkillsClick}
              
            >
              Identify Skills {"\u200B"}
              <AutoAwesomeIcon />
            </Button>
          </Box>

          {/* Sample Texts Section - 50% of left half */}
          <Box sx={{ height: '50%', overflow: 'auto' }}>
            <List sx={{ width: '100%' }}>
              <ListItem>
                <ListItemText 
                  primary="We're seeking a Junior Software Developer to join our engineering team. This role involves building web applications using React and Node.js, writing clean code, and participating in code reviews. The ideal candidate has a CS degree or bootcamp certification, at least 1 year of coding experience, and strong JavaScript skills. Remote position."
                  sx={{ mr: 2 }}
                />
                <Button 
                  variant="outlined" 
                  onClick={() => handleSampleTextClick("We're seeking a Junior Software Developer to join our engineering team. This role involves building web applications using React and Node.js, writing clean code, and participating in code reviews. The ideal candidate has a CS degree or bootcamp certification, at least 1 year of coding experience, and strong JavaScript skills. Remote position.")}
                >
                  Use
                </Button>
              </ListItem>
              <ListItem>
                <ListItemText 
                  primary="Our marketing team needs a Marketing Coordinator based in New York. You'll manage our social media presence, create engaging marketing content, and track campaign performance. We're looking for someone with a Bachelor's degree, 1-2 years of marketing experience, and proven social media expertise. Full-time position with competitive benefits."
                  sx={{ mr: 2 }}
                />
                <Button 
                  variant="outlined" 
                  onClick={() => handleSampleTextClick("Our marketing team needs a Marketing Coordinator based in New York. You'll manage our social media presence, create engaging marketing content, and track campaign performance. We're looking for someone with a Bachelor's degree, 1-2 years of marketing experience, and proven social media expertise. Full-time position with competitive benefits.")}
                >
                  Use
                </Button>
              </ListItem>
              <ListItem>
                <ListItemText 
                  primary="Join our analytics team as a Data Analyst in our hybrid work environment. You'll analyze data using SQL and Python, create reports and dashboards, and present insights to stakeholders. Requirements include an analytics-related degree, strong SQL skills, and experience with Tableau. This role offers opportunities for growth and development."
                  sx={{ mr: 2 }}
                />
                <Button 
                  variant="outlined" 
                  onClick={() => handleSampleTextClick("Join our analytics team as a Data Analyst in our hybrid work environment. You'll analyze data using SQL and Python, create reports and dashboards, and present insights to stakeholders. Requirements include an analytics-related degree, strong SQL skills, and experience with Tableau. This role offers opportunities for growth and development.")}
                >
                  Use
                </Button>
              </ListItem>
            </List>
          </Box>
        </Box>

        {/* Right Section: Display HTML */}
        <Box
          sx={{
            width: '50%',
          }}
        >
          <Paper sx={{ mt:2, margin:2, padding: 0, width: '100%', height: '100%', overflowY: 'auto',overflowX:'auto' }}>
  <div>
    {htmlContent ? (
      <div
        dangerouslySetInnerHTML={{ __html: htmlContent }}
        style={{
          wordWrap: 'break-word',
          whiteSpace: 'normal',
          overflowY: 'auto',
          maxHeight: 'calc(100vh - 120px)',
          padding: '10px',
          boxSizing: 'border-box',
          lineHeight: '1.6',
        }}
      />
    ) : (
      <div style={{
        textAlign: 'center',
        padding: '20px',
        color: '#999',
        fontSize: '16px',
      }}>
        Skills will be highlited once you enter a job description and click "Identify Skills".
      </div>
    )}
  </div>
</Paper>

        </Box>
      </Box>
    </AppTheme>
  );
}