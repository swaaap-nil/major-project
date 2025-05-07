import { BasicNvlWrapper } from '@neo4j-nvl/react'

export default () => <BasicNvlWrapper
 nodes={[{ id: '0' }, { id: '1' }]}
 rels={[{ id: '10', from: '0', to: '1' }]}
 nvlOptions={{ initialZoom: 2 }}
 nvlCallbacks={{ onLayoutDone: () => console.log('layout done') }}
/>