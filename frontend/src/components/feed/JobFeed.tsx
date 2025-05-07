import React, { useEffect, useState } from 'react';
import {
  Container,
  Paper,
  Typography,
  Box,
  Card,
  CardContent,
  Chip,
  IconButton,
  Link,
  Alert,
  Stack,
  useTheme
} from '@mui/material';
import {
  NotificationsActive as NotificationsActiveIcon,
  Launch as LaunchIcon,
  Circle as CircleIcon
} from '@mui/icons-material';

type Job = {
  job_id: string;
  title: string;
  company: string;
  location: string;
  link: string;
};

const WEBSOCKET_URL = "ws://localhost:8000/jobfeed";
const MAX_JOBS = 6;

const JobFeed: React.FC = () => {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [connected, setConnected] = useState(false);
  const theme = useTheme();

  useEffect(() => {
    const socket = new WebSocket(WEBSOCKET_URL);

    socket.onopen = () => {
      console.log("✅ Connected to WebSocket");
      setConnected(true);
    };

    socket.onmessage = (event) => {
      const job: Job = JSON.parse(event.data) as Job;
      setJobs(prevJobs => [job, ...prevJobs].slice(0, MAX_JOBS));
    };

    socket.onclose = () => {
      console.log("❌ Disconnected from WebSocket");
      setConnected(false);
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Paper
        elevation={3}
        sx={{
          p: 3,
          bgcolor: theme.palette.mode === 'dark' ? 'background.paper' : 'grey.50'
        }}
      >
        {/* Header */}
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 3, justifyContent: 'space-between' }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <NotificationsActiveIcon color="primary" />
            <Typography variant="h5" component="h1">
              Live Job Feed
            </Typography>
          </Box>
          <Chip
            icon={<CircleIcon sx={{ fontSize: '12px !important' }} />}
            label={connected ? "Connected" : "Disconnected"}
            color={connected ? "success" : "error"}
            variant="outlined"
            size="small"
          />
        </Box>

        {/* Connection Alert */}
        {!connected && (
          <Alert severity="error" sx={{ mb: 3 }}>
            Unable to connect to the job feed. Please check your connection.
          </Alert>
        )}

        {/* Jobs List */}
        <Box
          sx={{
            height: '32rem',
            overflowY: 'auto',
            '&::-webkit-scrollbar': {
              width: '8px',
            },
            '&::-webkit-scrollbar-track': {
              background: theme.palette.mode === 'dark' ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.1)',
              borderRadius: '4px',
            },
            '&::-webkit-scrollbar-thumb': {
              background: theme.palette.mode === 'dark' ? 'rgba(255,255,255,0.2)' : 'rgba(0,0,0,0.2)',
              borderRadius: '4px',
              '&:hover': {
                background: theme.palette.mode === 'dark' ? 'rgba(255,255,255,0.3)' : 'rgba(0,0,0,0.3)',
              },
            },
          }}
        >
          {jobs.length === 0 ? (
            <Box
              sx={{
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'text.secondary',
              }}
            >
              <Typography variant="h6" gutterBottom>
                No jobs available yet! 🚀
              </Typography>
              <Typography variant="body1">
                Stay tuned for new job listings.
              </Typography>
            </Box>
          ) : (
            <Stack spacing={2}>
              {jobs.map((job, index) => (
                <Card
                  key={job.job_id}
                  sx={{
                    transition: 'all 0.2s ease-in-out',
                    '&:hover': {
                      transform: 'translateY(-2px)',
                      boxShadow: theme.shadows[4],
                    },
                    opacity: 1 - index * 0.1,
                  }}
                >
                  <CardContent>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 1 }}>
                      <Typography variant="h6" component="h2" sx={{ color: 'primary.main' }}>
                        {job.title}
                      </Typography>
                      <IconButton
                        component={Link}
                        href={job.link}
                        target="_blank"
                        rel="noopener noreferrer"
                        size="small"
                        sx={{ ml: 1 }}
                      >
                        <LaunchIcon fontSize="small" />
                      </IconButton>
                    </Box>
                    <Box sx={{ display: 'flex', gap: 1 }}>
                      <Chip
                        label={job.company}
                        size="small"
                        color="secondary"
                        variant="outlined"
                      />
                      <Chip
                        label={job.location}
                        size="small"
                        variant="outlined"
                      />
                    </Box>
                  </CardContent>
                </Card>
              ))}
            </Stack>
          )}
        </Box>
      </Paper>
    </Container>
  );
};

export default JobFeed;