import { styled } from '@mui/material/styles';
import Typography from '@mui/material/Typography';
import Breadcrumbs, { breadcrumbsClasses } from '@mui/material/Breadcrumbs';
import NavigateNextRoundedIcon from '@mui/icons-material/NavigateNextRounded';

const StyledBreadcrumbs = styled(Breadcrumbs)(({ theme }) => ({
  margin: theme.spacing(1, 0),
  [`& .${breadcrumbsClasses.separator}`]: {
    color: (theme.vars || theme).palette.action.disabled,
    margin: 1,
  },
  [`& .${breadcrumbsClasses.ol}`]: {
    alignItems: 'center',
  },
}));

interface HomeBreadcrumbProps {
  path: string[]; // Make path optional
}

export default function NavbarBreadcrumb({ path }: HomeBreadcrumbProps) {
  if (!path || path.length === 0) {
    return null; // Return nothing if path is empty
  }

  return (
    <StyledBreadcrumbs
      aria-label="breadcrumb"
      separator={<NavigateNextRoundedIcon fontSize="small" />}
    >
      {path.map((item, index) => (
        <Typography
          key={index}
          variant="body1"
          sx={index === path.length - 1 ? { color: 'text.primary', fontWeight: 600 } : {}}
        >
          {item}
        </Typography>
      ))}
    </StyledBreadcrumbs>
  );
}