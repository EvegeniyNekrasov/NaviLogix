import { createLazyFileRoute } from '@tanstack/react-router'

export const Route = createLazyFileRoute('/routes')({
  component: () => <div>Hello /routes!</div>,
})
