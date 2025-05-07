import { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { columns } from '../internals/data/gridData';

const WEBSOCKET_URL = 'ws://3.111.45.66:8000/jobfeed';
const STORAGE_KEY = 'lastJobFeed'; // LocalStorage key

export default function CustomizedDataGrid() {
  const [connected, setConnected] = useState(false);
  const [rows, setRows] = useState<any[]>([]);
  const maxRows = 50; // Keep only the latest 50 jobs

  useEffect(() => {
    // Load persisted jobs from localStorage
    const savedJobs = localStorage.getItem(STORAGE_KEY);
    if (savedJobs) {
      setRows(JSON.parse(savedJobs) as any[]);
      console.log(savedJobs)
    }


    const socket = new WebSocket(WEBSOCKET_URL);

    socket.onopen = () => {
      console.log('✅ Connected to WebSocket');
      setConnected(true);
    };

    socket.onmessage = (event) => {
      try {
        const newJob = JSON.parse(event.data);

        setRows((prevRows) => {
          const updatedRows = [newJob, ...prevRows]; // Add new job at the top
          const limitedRows = updatedRows.length > maxRows ? updatedRows.slice(0, maxRows) : updatedRows;

          // Persist data to localStorage
          localStorage.setItem(STORAGE_KEY, JSON.stringify(limitedRows));

          return limitedRows;
        });
      } catch (error) {
        console.error('Error parsing WebSocket message:', error);
      }
    };

    socket.onclose = () => {
      console.log('❌ WebSocket Disconnected');
      setConnected(false);
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
      <DataGrid
        checkboxSelection
        rows={rows}
        columns={columns}
        getRowId={(row) => row.job_id}
        getRowClassName={(params) =>
          params.indexRelativeToCurrentPage % 2 === 0 ? 'even' : 'odd'
        }
        initialState={{
          pagination: { paginationModel: { pageSize: 20 } },
        }}
        pageSizeOptions={[10, 20, 50]}
        disableColumnResize
        density="compact"
        slotProps={{
          filterPanel: {
            filterFormProps: {
              logicOperatorInputProps: {
                variant: 'outlined',
                size: 'small',
              },
              columnInputProps: {
                variant: 'outlined',
                size: 'small',
                sx: { mt: 'auto' },
              },
              operatorInputProps: {
                variant: 'outlined',
                size: 'small',
                sx: { mt: 'auto' },
              },
              valueInputProps: {
                InputComponentProps: {
                  variant: 'outlined',
                  size: 'small',
                },
              },
            },
          },
        }}
      />
  );
}
