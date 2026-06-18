<template>
  <main class="min-h-screen bg-slate-50 px-4 py-10 text-slate-950">
    <div class="mx-auto flex max-w-4xl flex-col items-center gap-8">
      <div class="max-w-2xl text-center">
        <p class="text-sm font-semibold uppercase tracking-wide text-blue-700">B2B Analytics</p>
        <h1 class="mt-3 text-4xl font-bold tracking-tight">Company Health Dashboard</h1>
        <p class="mt-3 text-slate-600">
          Demo widget that requests a company score through a Nuxt server-side proxy.
        </p>
      </div>

      <CompanyScoreWidget company-id="4c9c1287-9786-4b4d-8c33-dba6c9c4d86f" />
    </div>
  </main>
</template>
