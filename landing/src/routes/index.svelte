<script context="module">
	export const router = false;
	const pdfURL = import.meta.env.VITE_PDF_URL ? String(import.meta.env.VITE_PDF_URL) : null;
</script>

<script>
	import { onMount } from 'svelte';
	import { Icon } from '@steeze-ui/svelte-icon';
	import { BookOpen, DocumentDownload, Code } from '@steeze-ui/heroicons';
	import { Facebook, Linkedin, Twitter } from '@steeze-ui/feather-icons';
	import Cite from '$lib/Cite.svelte'

	const entrypoints = [
		{
			icon: BookOpen,
			title: 'HTML',
			text: 'Read in your browser!',
			url: 'docs/html/index.html'
		},
		{
			icon: DocumentDownload,
			title: 'PDF',
			text: 'Download and read offline!',
			url: pdfURL ?? 'docs/addressinguncertaintyinmultisectordynamicsresearch.pdf',
		},
		{
			icon: Code,
			title: 'Source Code',
			text: 'Browse ebook source code!',
			url: 'https://github.com/IMMM-SFA/msd_uncertainty_ebook'
		}
	];

	const topics = [
		{
			text: 'An overview of diagnostic modeling and perspectives on model evaluation.',
			image: 'images/idealized_uc.png'
		},
		{
			text: 'A framework for the basic methods and concepts used in sensitivity analysis.',
			image: 'images/predator_prey.png'
		},
		{
			text: 'Technical applications supporting diagnostic model evaluation and exploration.',
			image: 'images/fishery_output.png'
		}
	];

	let myUrl = '';
	let fbShare = '';
	let twitterShare = '';
	let linkedinShare = '';

	onMount(() => {
		document.title = 'Addressing Uncertainty';
		myUrl = encodeURIComponent(window?.location?.href ?? '');
		fbShare = `https://www.facebook.com/sharer.php?u=${myUrl}`;
		twitterShare = `https://twitter.com/intent/tweet?url=${myUrl}&text=Check%20out%20this%20eBook%3A%20Addressing%20Uncertainty%20in%20MultiSector%20Dynamics%20Research&hashtags=DOE,IM3,MultiSectorDynamics`;
		linkedinShare = `https://www.linkedin.com/shareArticle?mini=true&url=${myUrl}&title=Check%20out%20this%20eBook%3A%20Addressing%20Uncertainty%20in%20MultiSector%20Dynamics%20Research&summary=Open%20access%20eBook%20showcasing%20sensitivity%20analysis%20and%20diagnostic%20model%20evaluation%20techniques.`;
	});
</script>

<div class="w-full flex flex-col lg:flex-row items-center justify-center py-6 px-3">
	<div class="max-w-xs lg:mr-6">
		<img class="w-full object-contain" src="images/ebook_thumbnail_1.png" alt="eBook" />
	</div>
	<div
		style="background-image: url('images/banner.png'); background-size: auto 234px; background-position: 6px 42px;"
		class="bg-no-repeat pl-3 lg:pl-56 py-12"
	>
		<div
			style="text-indent:-16px;"
			class="text-3xl font-bold text-slate-50 text-shadow pb-1 px-3 text-center lg:text-left leading-tight backdrop-blur-sm"
		>
			Addressing Uncertainty in<br />MultiSector Dynamics Research
		</div>
		<div class="h-16 border-y-4 border-slate-50 border-double" />
		<div
			class="text-md italic text-slate-50 text-shadow pt-1 px-3 text-center lg:text-left leading-tight backdrop-blur-sm"
		>
			<div style="">Patrick M. Reed, Antonia Hadjimichael, Keyvan Malek,</div>
			<div style="text-indent: -8px;">
				Tina Karimi, Chris R. Vernon, Vivek Srikrishnan, Rohini S. Gupta,
			</div>
			<div style="text-indent: -16px;">David F. Gold, Ben Lee, Klaus Keller, Travis B. Thurber, Jennie S. Rice</div>
		</div>
	</div>
</div>
<div
	class="w-full bg-slate-50 text-xl text-slate-900 py-6 px-3 flex flex-row items-center justify-around text-center xl:rounded-md"
>
	<div class="hidden md:block font-['ornaments'] text-slate-500 text-4xl mx-6">p</div>
	<div class="max-w-4xl">
		A living guide to sensitivity analysis and diagnostic model evaluation techniques for
		confronting the computational and conceptual challenges of multi-model, transdisciplinary
		workflows.
	</div>
	<div class="hidden md:block font-['ornaments'] text-slate-500 text-4xl mx-6">o</div>
</div>
<div class="w-full flex flex-col items-center justify-center text-center px-3 pb-6">
	<div class="text-2xl font-bold text-slate-50 my-6">GET THE EBOOK</div>
	<div
		class="flex flex-row flex-wrap items-center justify-around w-full border-y-4 border-double border-slate-50"
	>
		{#each entrypoints as entry}
			<a
				target="_blank"
				href={entry.url}
				class="flex-none flex flex-col items-center justify-center w-64 pt-3 pb-6 group"
			>
				<Icon src={entry.icon} class="icon w-20 text-slate-50 group-hover:text-sky-500" />
				<div class="text-xl font-bold text-slate-50 group-hover:text-sky-500">
					{entry.title}
				</div>
				<div class="text-md text-slate-50 group-hover:text-sky-500">
					{entry.text}
				</div>
			</a>
		{/each}
	</div>
</div>
<div class="w-full flex flex-col items-center justify-center text-center px-3 lg:pb-6">
	<div class="text-2xl font-bold text-slate-50 my-3">TOPICS IN THE BOOK</div>
	<div class="flex flex-col lg:flex-row items-center lg:items-start justify-around mt-6 w-full">
		{#each topics as topic, i}
			<div class="bg-slate-50 w-80 flex-none mb-12 lg:mb-0 shadow-md rounded-md">
				<div class="flex flex-row items-start justify-start text-left mb-3">
					<div
						class="bg-slate-900 w-20 h-20 flex-none flex items-center justify-center rounded-br-md"
					>
						<div class="text-4xl font-bold text-slate-50 text-shadow">
							{i + 1}
						</div>
					</div>
					<div class="text-md text-slate-900 mx-3 mt-3 leading-tight">
						{topic.text}
					</div>
				</div>
				<img class="w-full h-36 my-3 object-contain" src={topic.image} alt="" />
			</div>
		{/each}
	</div>
</div>
<div class="w-full flex flex-col items-center justify-center text-center px-3 pb-6">
	<div class="text-lg text-slate-50 lg:mt-6">Share with your network!</div>
	<div class="flex flex-row items-center justify-center mt-3 w-full">
		<a href={twitterShare} class="rounded-lg drop-shadow p-2 mx-3 bg-sky-700 hover:bg-sky-500">
			<Icon src={Twitter} class="icon w-6 text-slate-50" />
		</a>
		<a href={fbShare} class="rounded-lg drop-shadow p-2 mx-3 bg-sky-700 hover:bg-sky-500">
			<Icon src={Facebook} class="icon w-6 text-slate-50" />
		</a>
		<a href={linkedinShare} class="rounded-lg drop-shadow p-2 mx-3 bg-sky-700 hover:bg-sky-500">
			<Icon src={Linkedin} class="icon w-6 text-slate-50" />
		</a>
	</div>
</div>
<div class="w-full flex flex-col items-center justify-center text-center px-3 pb-12">
	<div class="text-lg text-slate-50 lg:mt-6">Cite the eBook!</div>
	<div class="flex flex-row items-center justify-center mt-3 w-full">
		<Cite />
	</div>
</div>
<div class="w-full flex flex-col items-center justify-center text-center px-3 pb-12">
	<div class="max-w-4xl text-sm italic text-slate-400">
		This e-book was developed by the <a
			href="https://im3.pnnl.gov"
			class="font-bold text-slate-500 hover:text-sky-700"
			>Integrated MultiSector, Multiscale Modeling (IM3)</a
		>
		project, supported by the
		<a href="https://www.energy.gov/" class="font-bold text-slate-500 hover:text-sky-700"
			>U.S. Department of Energy</a
		>,
		<a
			href="https://www.energy.gov/science/office-science"
			class="font-bold text-slate-500 hover:text-sky-700">Office of Science</a
		>, as part of research in the
		<a
			href="https://climatemodeling.science.energy.gov/program/multisector-dynamics"
			class="font-bold text-slate-500 hover:text-sky-700">MultiSector Dynamics</a
		>, Earth and Environmental System Modeling Program.
	</div>
</div>

<style>
	:global(.icon path) {
		stroke-width: 1;
	}
	.text-shadow {
		text-shadow: 1px 1px 1px rgba(33, 33, 33, 0.5);
	}
</style>
