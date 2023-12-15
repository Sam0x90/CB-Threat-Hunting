<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<div align="center">
<h1 align="center">CB-Threat-Hunting</h1>
    <a href="https://github.com/Sam0x90/CB-Threat-Hunting/issues">Report Bug</a>
    ·
    <a href="https://github.com/Sam0x90/CB-Threat-Hunting/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
# About The Project

Initially started by @0xAnalyst, I will try to update this repo with my humble contributions.\
It is meant to provide security analysts a 'cheatsheet' or 'guideline' to be used alongside CarbonBlack Response

This repository will contain mainly 2 things:
- **Detections**: Search queries to help security analysts finding malicious activities.
- **LiveResponse**: Response actions via CB Live Response feature to help security analysts performing incident response activities.
- **Scripts**: Scripts leveraging the the CB Response API to perform various actions.

Please don't hesitate to propose any additional queries and response actions for inclusion in this repository.

# Roadmap

- [x] Redefine and document the git structure
- [x] Define rule format
- [x] Create a script to automate watchlist creation via API
- [x] Document usage guide
- [ ] Update old queries if needed
- [ ] Create new content

See the [open issues](https://github.com/0xAnalyst/DefenderATPQueries/issues) for a full list of proposed features (and known issues).

# Detection

## Detection rule format
The following describes the rule format used in this repository to document detection rules.\
YAML is the format and it is meant to be easy to use. It is also mapped with the API /v1/watchlist so that it can be easily automated via cbapi python module or for example a SOAR.

### Format
```
name: 
index_type: 
description: 
references: 
tags: 
search_query: 
on_hit: 
```

### name
String API argument when creating a watchlist.\
This represents the name of the watchlist.

### index_type
String API argument when creating a watchlist.\
This represents the index in which to search for this watchlist, its value must either be 'event' (for processes) or 'modules' (for binaries).

Values:
- events
- modules

### description
String API argument when creating a watchlist.\
Description of the watchlist. The more precise the better. It should also include things like false positives.

### references
This is not an API argument. However it's recommended to include it as part of the description field.\
Reference to links and documents. For example is the rule is a translation from a Sigma rule, the sigma rule reference should be documented here. 

### tags
This is not an API argument. However it's recommended to include it as part of the description field.\
This represents the tags that can be added to the watchlist. MITRE ATT&CK tactics, techniques and subtechniques should be added here. 

### search_query
String API argument when creating a watchlist.\
This represents the query that will search into the index_type specified. 

### on_hit
This is not an API argument and must be check manually (please open PR/Issue if you found out how to define through API).\
This represents the different checkbox that can be checked to define the notification action(s) to trigger when the query hits.

Values:
- email_me
- create_alert
- log_to_syslog

### Example

[file_download_via_bitsadmin.yaml](https://github.com/Sam0x90/CB-Threat-Hunting/blob/master/Detections/file_download_via_bitsadmin.yaml)
```
name: File Download via Bitsadmin Usage
index_type: events
description: Detects the usage of the Windows built-in bitsadmin to download a file (especially with the transfer argument).
references: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download.yml
tags: c2, defense_evasion, s0190, t1197, t1105
search_query: process_name:"bitsadmin.exe" AND cmdline:"/transfer"
on_hit: create_alert, log_to_syslog
```

# LiveResponse
You will find [here](https://github.com/Sam0x90/CB-Threat-Hunting/blob/master/LiveResponse/README.md) the cheatsheet/guideline that will help security analysts on how to perform various response actions through the CarbonBlack EDR Live Response feature.\
The response actions categories are inspired from the ones defined in the [RE&CT framework](https://github.com/atc-project/atc-react).\
Here they are in alphabetic order: 
- :e-mail: Email
- :page_facing_up: File
- :key: Identity
- :globe_with_meridians: Network
- :space_invader: Process
- :computer: System (Configuration in RE&CT)


# Scripts

## Detection automation
In CarbonBlack world, a detection is called a watchlist.\
Once you've selected and downloaded the watchlists of your interest, place them all in a single folder.
You can then use the script [watchlist_create.py](https://github.com/Sam0x90/CB-Threat-Hunting/blob/master/Scripts/API/watchlist_create.py) to "bulk" create all the selected watchlists in your CB Response instance via API. 

The script will concatenate the fields 'references', 'tags' and 'on_hit' into the 'description' field and call the ```/v1/watchlist``` API endpoint to create the watchlists selected.\
You can read about those fields in [Detection rule format](https://github.com/Sam0x90/CB-Threat-Hunting/tree/master?tab=readme-ov-file#detection-rule-format).


|<img width="472" alt="image" src="https://github.com/Sam0x90/CB-Threat-Hunting/assets/13771868/3dd3acac-2652-4a21-b518-29398afc0878">|
|:--:| 
| *Script result for 2 yaml files* |


|<img width="1263" alt="image" src="https://github.com/Sam0x90/CB-Threat-Hunting/assets/13771868/2002d467-8db6-4537-9893-393a4565cbf5">|
|:--:| 
| *POST requests* |


> [!WARNING]  
> Still need to properly test the script, but first results are looking good :).

<!-- CONTRIBUTING -->
# Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

<!-- LICENSE -->
# License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- ACKNOWLEDGMENTS -->
# Acknowledgments

* []() https://github.com/0xAnalyst/CB-Threat-Hunting

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Sam0x90/CB-Threat-Hunting.svg?style=for-the-badge
[contributors-url]: https://github.com/Sam0x90/CB-Threat-Hunting/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Sam0x90/CB-Threat-Hunting.svg?style=for-the-badge
[forks-url]: https://github.com/Sam0x90/CB-Threat-Hunting/forks
[stars-shield]: https://img.shields.io/github/stars/Sam0x90/CB-Threat-Hunting.svg?style=for-the-badge
[stars-url]: https://github.com/Sam0x90/CB-Threat-Hunting/stargazers
[issues-shield]: https://img.shields.io/github/issues/Sam0x90/CB-Threat-Hunting.svg?style=for-the-badge
[issues-url]: https://github.com/Sam0x90/CB-Threat-Hunting/issues
[license-shield]: https://img.shields.io/github/license/Sam0x90/CB-Threat-Hunting.svg?style=for-the-badge
[license-url]: https://github.com/Sam0x90/CB-Threat-Hunting/blob/master/LICENSE
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
