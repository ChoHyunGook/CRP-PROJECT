import * as React from 'react';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';

const Copyright: React.FC = () => {
    return (
      <Typography variant="body2" color="text.secondary" align="center">
        {'Copyright © '}
        <Link color="#009688" href = '/'>
          CRP WebSite
        </Link>{' '}
        {new Date().getFullYear()}
      </Typography>
    );
}

const QA: React.FC = () => {
  return(
  <Typography variant='body2' color = "text.secondary" align = "center">
  <Link color = "#009688"href = "/company/profile" align-right={100}>
    개발자들       
    </Link>
    &nbsp; &nbsp;
  <Link color = "#009688"href = "/company/oursite">
    사이트 소개 
  </Link>
  &nbsp; &nbsp;
  <Link color = "#009688"href = "/company/aboutSite">
    관련사이트 
  </Link>
  &nbsp;&nbsp;
  </Typography>
  )
}
  
  
const Footer: React.FC = () => {
    return (
      <Box component="footer" sx={{ bgcolor: 'background.paper', py: 6 }}>
        <Container maxWidth="lg">
          <Typography variant="h6" align="center" gutterBottom >
          </Typography>
          <Typography
            variant="subtitle1"
            align="center"
            color="text.secondary"
            component="p"
          >
          </Typography>
          <Copyright />
          <QA />
        </Container>
      </Box>

      
    );
  }
  
export default Footer