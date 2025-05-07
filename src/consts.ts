import type { IconMap, SocialLink, Site } from '@/types'

export const SITE: Site = {
  title: 'Eli’s Blog',
  description:
    'A blog about software development, design, Arabic, FOSS, cryptoeconomics, libre graphics, and other things Eli is interested in.',
  href: 'https://elih.blog',
  author: 'Eli Heuer',
  locale: 'en-US',
  featuredPostCount: 3,
  postsPerPage: 3,
}

export const NAV_LINKS: SocialLink[] = [
  {
    href: '/projects',
    label: 'projects',
  },
  {
    href: '/graphics',
    label: 'graphics',
  },
  {
    href: '/tags',
    label: 'tags',
  },
  {
    href: '/about',
    label: 'about',
  },
]

export const SOCIAL_LINKS: SocialLink[] = [
  {
    href: 'https://github.com/eliheuer',
    label: 'GitHub',
  },
  {
    href: 'https://twitter.com/eliheuer',
    label: 'Twitter',
  },
  {
    href: 'mailto:elih@protonmail.com',
    label: 'Email',
  },
  {
    href: '/rss.xml',
    label: 'RSS',
  },
]

export const ICON_MAP: IconMap = {
  Website: 'lucide:globe',
  GitHub: 'lucide:github',
  LinkedIn: 'lucide:linkedin',
  Twitter: 'lucide:twitter',
  Email: 'lucide:mail',
  RSS: 'lucide:rss',
}
