import React, { useEffect, useRef } from 'react';
import { Graph } from '@antv/g6';

// Define TypeScript interfaces
interface Node {
  id: string;
  [key: string]: any;
}

interface Edge {
  id: string;
  source: string;
  target: string;
  [key: string]: any;
}

interface GraphData {
  nodes: Node[];
  edges: Edge[];
}

const format = (data: GraphData) => {
  const { nodes, edges } = data;
  return {
    nodes: nodes.map(({ id, ...node }) => ({ id, data: node })),
    edges: edges.map(({ id, source, target, ...edge }) => ({ id, source, target, data: edge })),
  };
};

const G6Graph: React.FC = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const graphRef = useRef<Graph | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://gw.alipayobjects.com/os/antvdemo/assets/data/xiaomi.json');
        const data = await response.json() as GraphData;

        if (containerRef.current) {
          graphRef.current = new Graph({
            container: containerRef.current,
            autoFit: 'view',
            data: format(data),
            behaviors: [
              {
                type: 'hover-activate',
                degree: 1,
              },
            ],
            layout: {
              type: 'force',
              preventOverlap: true,
              nodeSize: 24,
            },
            animation: false,
          });

          graphRef.current.render();
        }
      } catch (error) {
        console.error('Error fetching or rendering graph:', error);
      }
    };

    fetchData();

    // Cleanup function
    return () => {
      if (graphRef.current) {
        graphRef.current.destroy();
      }
    };
  }, []); // Empty dependency array means this effect runs once on mount

  return <div ref={containerRef} className="w-full h-96" />;
};

export default G6Graph;