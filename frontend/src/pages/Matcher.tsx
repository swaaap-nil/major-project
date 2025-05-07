import type {} from '@mui/x-date-pickers/themeAugmentation';
import type {} from '@mui/x-charts/themeAugmentation';
import type {} from '@mui/x-data-grid-pro/themeAugmentation';
import type {} from '@mui/x-tree-view/themeAugmentation';
import { alpha } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Input from '@mui/material/Input';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import AppTheme from '../shared-theme/AppTheme';
import SideMenu from '../dashboard/components/SideMenu';
import AppNavbar from '../dashboard/components/AppNavbar';
import { useState } from 'react';

export default function Matcher(props: { disableCustomTheme?: boolean }) {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0]??null);
    }
  };

  return (
    <AppTheme {...props} >
      <CssBaseline enableColorScheme />
      <Box sx={{ display: 'flex' }}>
        <SideMenu />
        <AppNavbar />
        {/* Main content */}
        <Box
          component="main"
          sx={(theme) => ({
            flexGrow: 1,
            backgroundColor: theme.vars
              ? `rgba(${theme.vars.palette.background.defaultChannel} / 1)`
              : alpha(theme.palette.background.default, 1),
            overflow: 'auto',
            p: 3,
          })}
        >
          {/* File Upload Section */}
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, alignItems: 'center' }}>
            <Input
              type="file"
              onChange={handleFileChange}
              inputProps={{ accept: '*/*' }}
              sx={{ display: 'none' }}
              id="file-upload"
            />
            <label htmlFor="file-upload">
              <Button
                variant="contained"
                component="span"
                startIcon={<CloudUploadIcon />}
              >
                Upload Resume
              </Button>
            </label>
            {file && <Box>Selected File: {file.name}</Box>}
          </Box>
        </Box>
      </Box>
    </AppTheme>
  );
}