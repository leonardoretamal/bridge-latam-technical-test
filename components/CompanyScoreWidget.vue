<script setup lang="ts">
type Grade = 'A' | 'B' | 'C' | 'D'

type DimensionScores = {
  governance: number
  innovation: number
  operations: number
  finance: number
  sustainability: number
}

type ScoreResponse = {
  company_id: string
  composite_score: number
  grade: Grade
  dimension_scores: DimensionScores
  computed_at: string
}

const props = defineProps<{
  companyId: string
}>()

const demoDimensions: DimensionScores = {
  governance: 80,
  innovation: 70,
  operations: 65,
  finance: 75,
  sustainability: 72,
}

const gradeClasses: Record<Grade, string> = {
  A: 'bg-emerald-100 text-emerald-800 ring-emerald-200',
  B: 'bg-blue-100 text-blue-800 ring-blue-200',
  C: 'bg-yellow-100 text-yellow-800 ring-yellow-200',
  D: 'bg-red-100 text-red-800 ring-red-200',
}

const dimensionLabels: Record<keyof DimensionScores, string> = {
  governance: 'Governance',
  innovation: 'Innovation',
  operations: 'Operations',
  finance: 'Finance',
  sustainability: 'Sustainability',
}

const score = ref<ScoreResponse | null>(null)
const isLoading = ref(true)
const errorMessage = ref<string | null>(null)
const dimensionEntries = computed(() => {
  if (!score.value) {
    return []
  }

  return Object.entries(score.value.dimension_scores) as [keyof DimensionScores, number][]
})

onMounted(async () => {
  try {
    score.value = await $fetch<ScoreResponse>('/api/score', {
      method: 'POST',
      body: {
        company_id: props.companyId,
        dimensions: demoDimensions,
      },
    })
  } catch {
    errorMessage.value = 'We could not load the company score. Please try again.'
  } finally {
    isLoading.value = false
  }
})
</script>

<template>
  <section class="w-full max-w-xl rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
    <div v-if="isLoading" class="space-y-5" aria-label="Loading company score">
      <div class="h-5 w-40 animate-pulse rounded bg-slate-200" />
      <div class="h-16 w-32 animate-pulse rounded-2xl bg-slate-200" />
      <div class="space-y-3">
        <div v-for="item in 5" :key="item" class="h-4 animate-pulse rounded bg-slate-200" />
      </div>
    </div>

    <div v-else-if="errorMessage" class="rounded-2xl bg-red-50 p-4 text-sm text-red-700">
      {{ errorMessage }}
    </div>

    <div v-else-if="score" class="space-y-6">
      <div class="flex items-start justify-between gap-4">
        <div>
          <p class="text-sm font-medium uppercase tracking-wide text-slate-500">Company Health</p>
          <p class="mt-2 text-5xl font-bold tracking-tight text-slate-950">
            {{ score.composite_score.toFixed(1) }}
          </p>
        </div>

        <span
          class="rounded-full px-4 py-2 text-sm font-bold ring-1"
          :class="gradeClasses[score.grade]"
        >
          Grade {{ score.grade }}
        </span>
      </div>

      <div class="space-y-4">
        <div
          v-for="[key, value] in dimensionEntries"
          :key="key"
          class="space-y-2"
        >
          <div class="flex items-center justify-between text-sm">
            <span class="font-medium text-slate-700">{{ dimensionLabels[key] }}</span>
            <span class="tabular-nums text-slate-500">{{ value.toFixed(1) }}/100</span>
          </div>

          <div class="h-3 overflow-hidden rounded-full bg-slate-100">
            <div
              class="h-full rounded-full bg-slate-900 transition-all duration-500"
              :style="{ width: `${value}%` }"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
