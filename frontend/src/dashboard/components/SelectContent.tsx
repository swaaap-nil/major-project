
import MuiAvatar from '@mui/material/Avatar';
import MuiListItemAvatar from '@mui/material/ListItemAvatar';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';
import { styled } from '@mui/material/styles';
import logo from '../../static/logo.png'

const Avatar = styled(MuiAvatar)(({ theme }) => ({
  width: 28,
  height: 28,
  backgroundColor: (theme.vars || theme).palette.background.paper,
  color: (theme.vars || theme).palette.text.secondary,
  border: `1px solid ${(theme.vars || theme).palette.divider}`,
}));

const ListItemAvatar = styled(MuiListItemAvatar)({
  minWidth: 0,
  marginRight: 12,
});

export default function SelectContent() {
  return (
    <List sx={{ width: 215, border: '1px solid #ddd', borderRadius: 1, p: 1 }}>
      <ListSubheader sx={{ pt: 0 }}>Development</ListSubheader>
      <ListItem >
        <ListItemAvatar>
        <Avatar alt="SkillMatcher Logo" src={logo} />
        </ListItemAvatar>
        <ListItemText primary="Skill Matcher" />
      </ListItem>
    </List>
  );
}
