import Avatar from '@mui/material/Avatar';
import Chip from '@mui/material/Chip';
import { GridCellParams, GridRowsProp, GridColDef } from '@mui/x-data-grid';
import { SparkLineChart } from '@mui/x-charts/SparkLineChart';

type SparkLineData = number[];

function renderStatus(status: 'Open' | 'Closed') {
  const colors: { [index: string]: 'success' | 'default' } = {
    Open: 'success',
    Closed: 'default',
  };

  return <Chip label={status} color={colors[status]} size="small" />;
}

export function renderAvatar(
  params: GridCellParams<{ name: string; color: string }, any, any>,
) {
  if (!params.value) {
    return '';
  }

  return (
    <Avatar
      sx={{
        backgroundColor: params.value.color,
        width: '24px',
        height: '24px',
        fontSize: '0.85rem',
      }}
    >
      {params.value.name.toUpperCase().substring(0, 1)}
    </Avatar>
  );
}

export const columns: GridColDef[] = [
  {field: 'timestamp',headerName:'Timestamp',minWidth:150},
  { field: 'title', headerName: 'Job Title', flex: 1.5, minWidth: 170 },
  {
    field: 'company',
    headerName: 'Company',
    flex: 1,
    minWidth: 150,
  },
  {
    field: 'status',
    headerName: 'Status',
    flex: 0.5,
    minWidth: 100,
    renderCell: (params) => renderStatus(params.value as any),
  },
  {
    field: 'location',
    headerName: 'Location',
    flex: 1,
    minWidth: 120,
  },
  {
    field: 'link',
    headerName: 'Apply Link',
    flex: 1,
    minWidth: 100,
    renderCell: (params) => (
      <a href={params.value} target="_blank" rel="noopener noreferrer">
        Apply Here
      </a>
    ),
  },
];

export const rows: GridRowsProp = [
  {
    id: 1,
    jobTitle: 'Software Engineer',
    companyName: 'Google',
    status: 'Open',
    location: 'San Francisco, CA',
    applyLink: 'https://careers.google.com/job/software-engineer',
  },
  {
    id: 2,
    jobTitle: 'Data Analyst',
    companyName: 'Microsoft',
    status: 'Open',
    location: 'Redmond, WA',
    applyLink: 'https://careers.microsoft.com/job/data-analyst',
  },
  {
    id: 3,
    jobTitle: 'Product Manager',
    companyName: 'Amazon',
    status: 'Closed',
    location: 'Seattle, WA',
    applyLink: 'https://amazon.jobs/job/product-manager',
  },
  {
    id: 4,
    jobTitle: 'UX Designer',
    companyName: 'Meta',
    status: 'Open',
    location: 'Menlo Park, CA',
    applyLink: 'https://www.metacareers.com/job/ux-designer',
  },
];
