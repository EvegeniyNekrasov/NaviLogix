import { createLazyFileRoute } from '@tanstack/react-router'

export const Route = createLazyFileRoute('/vessels')({
  component: () => <div>Hello /vessels!</div>,
})
