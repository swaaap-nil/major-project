export type FunctionComponent = React.ReactElement | null;

type HeroIconSVGProps = React.PropsWithoutRef<React.SVGProps<SVGSVGElement>> &
	React.RefAttributes<SVGSVGElement>;
type IconProps = HeroIconSVGProps & {
	title?: string;
	titleId?: string;
};
export type Heroicon = React.FC<IconProps>;

export interface GraphNode {
	id: string;
	label: string;
  }
  
  export interface GraphEdge {
	source: string;
	target: string;
  }
  